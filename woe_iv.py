#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd

def woe_iv(_df, target):
    df = _df.copy()
    df = df.fillna(0)
    df_woe_list = pd.DataFrame()
    var_list = [col for col in df.columns if col != target]
    for var in var_list:
        if df.dtypes[var] != 'object':
            conditions = [df[var] <= np.nanpercentile(df[var], i) for i in
                          np.arange(10, 110, 10)]
            categories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            df["decile_{}".format(var)] = np.select(conditions, categories,
                                                    default=np.nan)
            df_woe = df.groupby("decile_{}".format(var)).agg({
                var: {'min', 'max', 'count'}, target: 'sum'}).droplevel(
                0, axis=1).reset_index().rename(
                columns={"decile_{}".format(var): 'decile'})
            df_woe['type'] = 'numeric'
        elif df.dtypes[var] == 'object':
            df_woe = df.groupby(var).agg({
                var: {'count'}, target: {'sum'}}).droplevel(
                0, axis=1).reset_index().rename(columns={var: 'decile'})
            df_woe['min'] = np.nan
            df_woe['max'] = np.nan
            df_woe['type'] = 'categorical'
        df_woe2 = pd.DataFrame({'feature': var, 'type': df_woe['type'],
                                'decile': df_woe['decile'],
                                'min': df_woe['min'], 'max': df_woe['max'],
                                'cnt': df_woe['count'], 'target': df_woe['sum']
                                })
        df_woe2['target_rate'] = (df_woe2.target / df_woe2.cnt) * 100
        df_woe2['target_pct'] = (df_woe2.target / df_woe2.target.sum()) * 100
        df_woe2['nontarget_pct'] = ((df_woe2.cnt - df_woe2.target) / (
                df_woe2.cnt.sum() - df_woe2.target.sum())) * 100
        df_woe2['woe'] = np.log(df_woe2.nontarget_pct / df_woe2.target_pct)
        df_woe2['iv'] = ((df_woe2.nontarget_pct - df_woe2.target_pct) *
                         df_woe2.woe / 100).sum()
        df_woe_list = pd.concat([df_woe_list, df_woe2], axis=0)
        df_iv_list = df_woe_list.drop_duplicates(
            subset=['feature', 'iv'],
            keep="first")[['feature', 'iv']].sort_values('iv', ascending=False)

    return df_woe_list, df_iv_list

