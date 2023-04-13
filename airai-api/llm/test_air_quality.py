import unittest


class TestAirQualityModel(unittest.TestCase):

    def test_skip(self):
        """
        Skip this test. This test was written when we use GPT-3 model. Langchain chat model mocking is not
        documented yet. We will revisit this test when we have a better understanding of mocking.
        :return:
        """
        print("Skip this test. This test was written when we use GPT-3 model. Langchain chat model mocking is not "
              "documented yet. We will revisit this test when we have a better understanding of mocking.")

    # @patch('air_quality.get_llm')
    # def test_air_quality_model(self, mock_get_llm):
    #     mock_get_llm.return_value = FakeListLLM(
    #         responses=[
    #             '[{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954}]',
    #             'null',
    #             '[{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954}, {"name": "Paris", "latitude": 48.856614, "longitude": 2.352222}]',
    #             '[]',
    #         ])
    #     # Test valid input
    #     text = "What's the air quality in Berlin?"
    #     expected_output = [{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954}]
    #
    #     output = air_quality_model(text)
    #
    #     self.assertEqual(output, expected_output)
    #
    #     # Test null output
    #     text = "What's the weather in Berlin?"
    #     expected_output = None
    #     output = air_quality_model(text)
    #     self.assertEqual(output, expected_output)
    #
    #     # Test multiple city output
    #     text = "Compare the air quality in the capitals of Germany and France."
    #     expected_output = [{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954},
    #                        {"name": "Paris", "latitude": 48.856614, "longitude": 2.352222}]
    #     output = air_quality_model(text)
    #     self.assertEqual(output, expected_output)
    #
    #     # Test empty list output
    #     text = "How's the air quality?"
    #     expected_output = []
    #     output = air_quality_model(text)
    #     self.assertEqual(output, expected_output)
