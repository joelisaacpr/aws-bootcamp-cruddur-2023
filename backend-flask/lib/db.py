from psycopg_pool import ConnectionPool
import os

class Db:
  def __init__(self):
    self.init_pool()

  def init_pool():
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)
  # we want to commit data such as an insert
  def query_commit_returning_id(self,sql,*Kwargs):
    print("SQL STATEMENT-[commit with returning]---------")
 
    pattern =r"\bRETURNING\b"
    match = re.search(pattern, my_string)

    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql,*kwargs)
      returning_id = cur.fetchone()[0]

      
      conn.commit()
      return returning_id
    except Exception as err:
      self.print_sql_err(err)

  def query_commit(self,sql):
    print("SQL STATEMENT-[commit]--------")
    try:
      conn = self.pool.connection()
      cur = conn.cursor()
      cur.execute(sql)
      returning_id = cur.fetchone()[0]
      conn.commit()
      return returning_id
    except Exception as err:
      self.print_sql_err(err)

  # when we want to return a json object
  def query_array_json(self,sql):
    print("SQL STATEMENT-[array]---------")
    print(sql + "\n")
    print("")
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()

  # when we want to return an array of json objects
  def query_object_json(self,sql):
    print("SQL STATEMENT-[object]---------")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          json = cur.fetchone()
          return json[0]

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
  def print_sql_err(err):
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
db = Db