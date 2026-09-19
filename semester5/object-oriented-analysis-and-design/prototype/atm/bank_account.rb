module Bank
  class BankAccount
    class BalanceError < StandardError; end
    attr_reader :balance, :owner_id

    def initialize(customer_id, balance)
      unless balance.is_a?(Integer) && balance >= 0
        raise ArgumentError, 'Balance must be a nonnegative integer in minor currency units'
      end

      @owner_id = customer_id
      @balance = balance
    end

    def withdrawal(amount)
      validate_amount(amount)
      raise BalanceError, 'Insufficient funds for withdrawal' if amount > @balance

      @balance -= amount
    end

    def payment(amount)
      validate_amount(amount)
      @balance += amount
    end

    private

    def validate_amount(amount)
      unless amount.is_a?(Integer) && amount.positive?
        raise ArgumentError, 'Amount must be a positive integer in minor currency units'
      end
    end
  end
end
