query_nariz = """
            SELECT TOP 1 Value as value
            FROM History
            WHERE DateTime BETWEEN dateadd(HH, -1, getdate()) AND GETDATE()
            AND TagName IN (
                'PB22_P_L1_5_NARIZ.PV'
            )
            AND wwRetrievalMode = 'Interpolated'
            AND wwResolution = '60000'
            ORDER BY DateTime ASC
        """
query_energia = """
            SELECT TOP 1 Value as value
            FROM History
            WHERE DateTime BETWEEN dateadd(HH, -1, getdate()) AND GETDATE()
            AND TagName IN (
                'PB22_P_L1_2_Energ_Especifica_C1.PV'
            )
            AND wwRetrievalMode = 'Interpolated'
            AND wwResolution = '60000'
            ORDER BY DateTime ASC
        """
query_temp_manto = """
            SELECT TOP 1 Value as value
            FROM History
            WHERE DateTime BETWEEN dateadd(HH, -1, getdate()) AND GETDATE()
            AND TagName IN (
                'PB22_P_L1_4_Temp_Colchao.PV'
            )
            AND wwRetrievalMode = 'Interpolated'
            AND wwResolution = '60000'
            ORDER BY DateTime ASC
            """
query_insert_rate = """
            INSERT INTO IncubadoraResultados (datetime, description, value)
            VALUES
                (?, ?, ?)
            """
