from log import Log
from functions import Functions

from datetime import datetime
import time

from skmultiflow.meta import AdaptiveRandomForestRegressor

from queries import (
    query_nariz,
    query_energia,
    query_temp_manto,
    query_insert_rate,
)


def main():
    
    X = []
    ht_reg = AdaptiveRandomForestRegressor()
    func = Functions()

    while True:
        (nariz,) = func.get_sensor_info(query_nariz)[0]
        (energia,) = func.get_sensor_info(query_energia)[0]

        if nariz is not None and energia is not None:
            pred, taxa = 0, 0
            if nariz == 1 and energia > 80:
                (y,) = func.get_sensor_info(query_temp_manto)[0]
                y = round(y, 1)
                if len(X) >= 12:
                    ht_reg = func.fit(ht_reg, X, y)

                    X.append(y)

                    pred, taxa = func.pred(ht_reg, X)
                else:
                    X.append(y)

            else:
                X = []

            dados = (
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "taxa_var_temp_manto",
                taxa,
            )
            
            func.post_info(query_insert_rate, dados)

        time.sleep(60*5)

        if len(X) > 60:
            X.pop(0)


if __name__ == "__main__":
    main()
