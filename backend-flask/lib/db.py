from psycopg_pool import ConnectionPool
import os

def query_wrap_object(template):
  sql = f"""
  (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
  {template}
  ) object_row);
  """
  return sql

def query_wrap_array(template):
  sql = f"""
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
  {template}
  ) array_row);
  """
  return sql

def print_psycpg_err(err):
  # get details about the exception
  err_type, err_obj, traceback = sys.exc_info()

  # get the line number when exception occured
  line_num = traceback.tb_lineno

  # print the connect() error
  print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
  print ("psycopg2 traceback:", traceback, "-- type:", err_type)

  # psycopgn2 extension.Diagnostics object attribute
  print ("\nextensions.Diagnostics:", err.diag)

  # print the pgcode and pferror exceptions
  print ("pgerror:", err.pgerror)
  print ("pgcode:", err.pgcode, "\n")
  
connection_url = os.getenv("CONNECTION_URL")
pool = ConnectionPool(connection_url)