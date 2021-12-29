require 'pg'
require 'dotenv'

Dotenv.load

begin

  conn = PG.connect(:dbname => ENV['DBNAME'],:user = ENV['USER'],:password => ENV['PASSWORD'])
  rs = conn.exec "SELECT * FROM Pisarze"
  rs.each { |row| p row }

rescue PG::Error => e

  puts e.message
ensure

  rs.clear if rs
  conn.close if conn
end


