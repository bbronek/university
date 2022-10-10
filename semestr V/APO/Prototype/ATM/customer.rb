# frozen_string_literal: true
module Bank
  class Customer
    attr_reader :id

    @@customers_number ||= 0

    def self.create(first_name, last_name)
      @@customers_number += 1
      new(first_name, last_name, @@customers_number)
    end

    def initialize(first_name, last_name, id)
      @first_name = first_name
      @last_name = last_name
      @id = id
    end
  end
end


