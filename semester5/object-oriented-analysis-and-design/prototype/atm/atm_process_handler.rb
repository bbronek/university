# frozen_string_literal: true

require_relative 'bank_account'
require_relative 'cards/bank_card'

module Bank
  module Atm
    class AtmProcessHandler
      attr_reader :errors

      def self.handle(card, bank_account)
        return unless card && card.owner_id == bank_account.owner_id

        new(bank_account) if Cards::BankCard::PinValidator.validate(card.pin).empty?
      end

      def initialize(bank_account)
        @bank_account = bank_account
        @errors = []
      end

      def withdraw(amount)
        @bank_account.withdrawal(amount)
      rescue Bank::BankAccount::BalanceError => e
        @errors << e.message
      end

      def deposit(amount)
        @bank_account.payment(amount)
      end

      def buy_pre_paid_codes(number)
        raise ArgumentError, "Code count must be a positive integer" unless number.is_a?(Integer) && number.positive?

        price = 50
        @bank_account.withdrawal(price * number)
      end

      def check_balance
        @bank_account.balance
      end

      def transfer(transfer_account, amount)
        raise ArgumentError, "Expected a bank account" unless transfer_account.is_a?(Bank::BankAccount)

        @bank_account.withdrawal(amount)
        transfer_account.payment(amount)
      end
    end
  end
end
