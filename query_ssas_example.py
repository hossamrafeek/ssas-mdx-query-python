"""
Author: Hossam Rafeek
Purpose: Query SSAS Tabular Data Using Python and ADOMD.NET

"""

from System import DBNull
from Microsoft.AnalysisServices.AdomdClient import AdomdConnection, AdomdCommand

# Connection Settings - Update these for your environment
SERVER_NAME = "YOUR_SSAS_SERVER"
DATABASE_NAME = "YOUR_DATABASE_NAME"

# Connection
conn_str = f"Data Source={SERVER_NAME};Initial Catalog={DATABASE_NAME};Integrated Security=SSPI"
conn = AdomdConnection(conn_str)
conn.Open()

# MDX Query - Example: Get 'S_Value' measure grouped by 'Year'
query = """
SELECT 
  {[Measures].[S_Value]} ON COLUMNS,
  NON EMPTY 
    [DimDate].[Year].MEMBERS ON ROWS
FROM [YOUR_CUBE_NAME]
"""

# Execute query
cmd = AdomdCommand(query, conn)
reader = cmd.ExecuteReader()

# Print column headers
for i in range(reader.FieldCount):
    print(reader.GetName(i), end='\t')
print()

# Print data rows
while reader.Read():
    for i in range(reader.FieldCount):
        value = reader.GetValue(i)
        if value == DBNull.Value:
            print("NULL", end='\t')
        else:
            print(value, end='\t')
    print()

# Close connections
reader.Close()
conn.Close()
