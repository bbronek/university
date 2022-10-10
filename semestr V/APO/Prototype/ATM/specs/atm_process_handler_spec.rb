# frozen_string_literal: true

require_relative '../atm'
require_relative '../customer'
require_relative '../bank_account'
require_relative '../cards/bank_card'
require_relative '../cards/payment_card'
require_relative '../atm_process_handler'

describe Bank::Atm::AtmProcessHandler do
  describe '#handle' do
    it 'should create new handler instance if card pin is valid' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)
      expect(handler).to be_an_instance_of(Bank::Atm::AtmProcessHandler)
    end

    it 'should return array of errors if pin is invalid' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('invalid', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)
      expect(handler).to eq(nil)
    end
  end

  describe '#withdraw' do
    it 'should withdraw money if account has enough resources' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)

      amount = 5000

      handler.withdraw(amount)

      expect(bank_account.balance).to eq(5000)
    end

    it 'should raise error if account doesn\'t have enough resources to perform withdraw operation' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)

      amount = 15_000
      handler.withdraw(amount)

      expect(handler.errors).to eq(["Insufficient resources to perform witdraw operation"])
    end
  end

  describe '#deposit' do
    it 'should depose given resources' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)

      amount = 5000

      handler.deposit(amount)

      expect(bank_account.balance).to eq(15_000)
    end
  end

  describe '#buy_pre_paid_codes' do
    it 'should perform pre paid codes purchase' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)

      number = 10

      handler.buy_pre_paid_codes(number)

      expect(bank_account.balance).to eq(9_500)
    end
  end

  describe '#check_balance' do
    it 'should print out bank account balance' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account)

      expect(handler.check_balance).to eq(bank_account.balance)
    end
  end

  describe '#transfer' do
    it 'should perform bank accounts transfer' do
      sample_customer1 = Bank::Customer.create('John', 'Doe')
      sample_customer2 = Bank::Customer.create('Jack', 'Daniels')
      bank_account1 = Bank::BankAccount.new(sample_customer1.id, 10_000)
      bank_account2 = Bank::BankAccount.new(sample_customer2.id, 5_000)

      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer1.id)

      handler = Bank::Atm::AtmProcessHandler.handle(payment_card, bank_account1)

      handler.transfer(bank_account2, 6_000)

      expect(bank_account1.balance).to eq(4_000)
      expect(bank_account2.balance).to eq(11_000)
    end
  end
end
