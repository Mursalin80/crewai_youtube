#!/usr/bin/env python
import sys
import warnings

from youtube.crew import Youtube

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    youtube_channel_handle = input("Please enter the YouTube handle to analyze:\n")
    Youtube().crew().kickoff(inputs={"youtube_channel_handle": youtube_channel_handle})


def train():
    """
    Train the crew for a given number of iterations.
    """
    youtube_channel_handle = input("Please enter the YouTube handle to analyze:\n")

    try:
        Youtube().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs={"youtube_channel_handle": youtube_channel_handle})

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Youtube().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    youtube_channel_handle = input("Please enter the YouTube handle to analyze:\n")
    
    try:
        Youtube().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs={"youtube_channel_handle": youtube_channel_handle})

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
