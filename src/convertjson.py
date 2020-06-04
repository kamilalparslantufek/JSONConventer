import pandas as pd
import mysql.connector


# defined class, cause we have more than one convert types
class Converter:
    def convert2csv(self, result):
        """[summary]Converts JSON to CSV

        Args:
            result ([dict]): [JSON File]

        Returns:
            [Pandas Dataframe]: [Converted to Dataframe saved as CSV]
        """
        # i tried parsing 2 different json files, one worked in top one other one
        # worked in bottom one so im keeping both of these methods, one fails other works
        # Errors i encountered are TypeError for index, valueError: DataFrame constructor not properly called
        # and ValueError: If using all scalar values, you must pass an index
        try:  # trying to get every key as columns in dataframe making all of them a list
            df = pd.DataFrame()
            for key in result.keys():
                key_df = pd.DataFrame(result[key])
                df = df.append(key_df)
        except:
            df = pd.DataFrame(result)
            df_res = pd.DataFrame()
            for key in df.keys():
                print(type(result[key]))
                key_df = pd.Series(df[key])
                df_res = df_res.append(key_df.to_frame().T)
            df_res.to_csv("result.csv")
            return df_res
        df.to_csv("result.csv")
        return df