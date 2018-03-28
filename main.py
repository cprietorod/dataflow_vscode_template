# https://beam.apache.org/documentation/programming-guide/
# https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/complete/game/hourly_team_score.py

import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def count(word):
    """count number of words"""
    return [len(word)]

def suma(val):
    """simple sum function"""
    return sum(val)

def run(known_args, argv):
    """ Main funtion that create pipeline and run it"""
    options = PipelineOptions(argv)

    pipeline = beam.Pipeline(options=options)
    
    words = "asdf asdf asdf asdf asdf asdf"
    lines = pipeline | 'create words' >> beam.Create(words.split(" "))

    result = lines | 'count words' >> beam.ParDo(count) \
    | 'sum' >> beam.CombineGlobally(sum) \
    | 'save' >> beam.io.WriteToText(known_args.output)

    result = pipeline.run()
    if options.get_all_options()['runner'] == "DirectRunner":
        result.wait_until_finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", dest="output", required=True)

    known, pipeline_args = parser.parse_known_args()

    run(known, pipeline_args)
