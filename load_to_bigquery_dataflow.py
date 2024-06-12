import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class DataIngestion:
    def parse_method(self, string_input):
        import json
        row = json.loads(string_input)
        return row

def run():
    project_id = 'quixotic-treat-419302'
    bucket = 'gs://bankingvm'
    dataset_id = 'transactions'
    table_id = 'credit'
    file_pattern = bucket + '/*.json'
    
    options = PipelineOptions(
        project=project_id,
        temp_location=bucket + '/temp',
        staging_location=bucket + '/staging',
        runner='DataflowRunner'
    )

    p = beam.Pipeline(options=options)

    (p
     | 'ReadData' >> beam.io.ReadFromText(file_pattern)
     | 'ParseJson' >> beam.Map(lambda x: json.loads(x))
     | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
            project=project_id,
            dataset=dataset_id,
            table=table_id,
            schema='SCHEMA_AUTODETECT',
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
        )
     )

    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
