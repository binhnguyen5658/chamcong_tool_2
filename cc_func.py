import pandas as pd

def transform_file(df):
    # --- Extract date ---
    first_date = df.iloc[3,0].split()[2]

    last_date = df.iloc[3,0].split()[-1]


    # --- filter valid data
    df_org = df.iloc[6:,:-5]

    # --- set new column header
    df_org.columns = df_org.iloc[0]

    #  --- filter useful row and columns
            #  Columns
    df_org.columns = df_org.columns.map(str)

    df_org = df_org.drop(columns=[ col for col in df_org.columns if col in ['nan', 'STT', 'Tên nhân viên']], axis=1)
            # Row  
    df_clean = df_org.loc[df_org['Ngày'].isin(['Vào đầu', 'Ra cuối'])].copy()

    df_clean['Mã nhân viên'] = df_clean['Mã nhân viên'].fillna(method='ffill')

    # --- pivot table and frop na row in col 'Time' --- 
    df_stack = (df_clean.melt(id_vars=['Mã nhân viên', 'Ngày'], 
                            var_name='Date', 
                            value_name='Time'
                            )
                        .copy()
                )
            
    df_stack =  df_stack[~df_stack['Time'].isna()]

    df_stack[['Date','Time']] = df_stack[['Date','Time']].astype('str')

    # --- Identify day of same or different month by datediff from the first date
    day_1 = first_date[:2]

    df_stack['Date_diff'] = df_stack['Date'].astype('int8') - int(day_1)

    first_my = first_date[3:]
    last_my = last_date[3:]

        #  --- format datetime required ---
    dt_format_1 = df_stack['Date'] + '/' + first_my + ' ' + df_stack['Time'].str[:5]
    dt_format_2 = df_stack['Date'] + '/' + last_my + ' ' + df_stack['Time'].str[:5]

    # --- concat date, month-year and time
        # same month
    df_stack['Thời gian'] = dt_format_1
        # different month
    df_stack.loc[df_stack['Date_diff'].astype('int8') < 0, 'Thời gian'] = dt_format_2

        # date < 10 need 0 ( format dd/mm/yyyy)
    df_stack.loc[df_stack['Date'].astype('int8') < 10, 'Thời gian'] = '0' + df_stack['Thời gian']

    df_stack = df_stack[['Mã nhân viên', 'Thời gian']]

    df_stack['Máy chấm công'] = 4

    # df_stack[['Mã nhân viên', 'Thời gian','Máy chấm công']] = df_stack[['Mã nhân viên', 'Thời gian','Máy chấm công']].astype('str')

    return df_stack