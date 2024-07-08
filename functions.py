import numpy as np
from scipy.signal import savgol_filter
import pyodbc
from session import Session


class Functions:
    def smoothing(self, X, slide_window, window, pow):
        ## Suavisa a curva de sensoriamento 
        return np.array([savgol_filter(X, window, pow)[-slide_window:]])

    def fit(self, model, X, y):
        ## Abastece o modelo com a primeira relação
        X_suave = self.smoothing(X, 12, 5, 3)
        return model.partial_fit(X_suave, np.array([y]))

    def pred(self, model, X):
        X_suave = self.smoothing(X, 12, 5, 3)

        ## Efetua a previsão e calcula a taxa de variação da temperatura
        pred = round(model.predict(X_suave)[0], 1)
        taxa = round((pred - X_suave[0][1]) / 6, 5)
        return pred, taxa

    def get_sensor_info(self, sql_query):
        cursor, connection = Session().create_session_sp()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        connection.close()

        return result

    def post_info(self, sql_query, dados):
        try:
            cursor, connection = Session().create_session_digiopc()
            cursor.execute(sql_query, dados)
            connection.commit()
            connection.close()
        except pyodbc.Error as e:
            print("Error executing SQL query:")
            print("SQL Query:", sql_query)
            print("Error Message:", e)
            # Optionally, log the error to a log file or logging system
            raise  # Re-raise the exception to propagate it further if needed

