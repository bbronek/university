require 'pg'
require 'dotenv/load'

PG.connect(dbname: ENV.fetch('DBNAME'), user: ENV.fetch('DBUSER'), password: ENV.fetch('PASSWORD')) do |connection|
  connection.exec(ENV.fetch('QUERY', 'SELECT * FROM writers')) do |rows|
    rows.each { |row| p row }
  end
end
