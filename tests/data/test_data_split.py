# Generated by CodiumAI


class TestSplitData:

    # Correctly splits data into train, test, and validation sets
    def test_correct_split(self):
        import pandas as pd
        from scripts.data_split import split_data

        data = pd.DataFrame({"col1": range(100)})
        train, test, validation = split_data(data)

        assert len(train) == 80
        assert len(test) == 10
        assert len(validation) == 10

    # Handles empty DataFrame input without errors
    def test_empty_dataframe(self):
        import pandas as pd
        from scripts.data_split import split_data

        data = pd.DataFrame()
        train, test, validation = split_data(data)

        assert train.empty
        assert test.empty
        assert validation.empty
