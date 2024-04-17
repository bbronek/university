# frozen_string_literal: true

module Bank
  class BankAccount
    class BalanceError < StandardError; end
    attr_reader :balance

    def initialize(customer_id, balance)
      @owner_id = customer_id
      @balance = balance
    end

    def withdrawal(amount)
      return @balance -= amount unless (@balance - amount).negative?

      raise BalanceError, 'Insufficient resources to perform witdraw operation'
    end

    def payment(amount)
      @balance += amount
    end
  end
end
