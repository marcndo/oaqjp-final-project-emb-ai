"""Test file for emotion detection 
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Test class for emotion detection.
    """

    def test_emotion_detection(self):
    """ Validates emotion detection functions
    by considering different test cases and comparing the functions output with
    the actual value. If all test passes we get an OK.
    """
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = emotion_detector("I am very mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = emotion_detector("I feel disgusted just hearing abut this")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')
        
        result5 = emotion_detector("I am really affraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')

unittest.main()