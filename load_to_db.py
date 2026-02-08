from db_connection import engine

from agg_insur_data import get_agg_insur_data

from agg_trans_data import get_agg_trans_data

from agg_user_data import get_agg_user_data

from map_insur_dist_data import get_map_insur_dist_data

from map_trans_data import get_map_trans_data

from map_user_data import get_map_user_data

from top_insur_dist_data import get_top_insur_dist_data

from top_insur_pin_data import get_top_insur_pin_data

from top_trans_dist_data import get_top_trans_dist_data

from top_trans_pin_data import get_top_trans_pin_data

from top_user_dist_data import get_top_user_dist_data

from top_user_pin_data import get_top_user_pin_data

tables = {
    'aggregated_insurance':get_agg_insur_data(),
    'aggregated_transaction':get_agg_trans_data(),
    'aggregated_user':get_agg_user_data(),
    'map_insurance':get_map_insur_dist_data(),
    'map_transaction':get_map_trans_data(),
    'map_user':get_map_user_data(),
    'top_insurance_district':get_top_insur_dist_data(),
    'top_insurance_pincode':get_top_insur_pin_data(),
    'top_transaction_district':get_top_trans_dist_data(),
    'top_transaction_pincode':get_top_trans_pin_data(),
    'top_user_district':get_top_user_dist_data(),
    'top_user_pincode':get_top_user_pin_data()
}


for table_name,df in tables.items():
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False
    )

    print(f"{table_name} is Pushed Successfully!!!")
    