# frozen_string_literal: true

require_relative '../atm'
require_relative '../customer'
require_relative '../bank_account'
require_relative '../cards/bank_card'
require_relative '../cards/payment_card'
require_relative '../atm_process_handler'

describe Bank::Atm::Atm do
  describe '#register_process' do
    it 'should register atm process' do
      sample_customer = Bank::Customer.create('John', 'Doe')
      payment_card = Bank::Cards::PaymentCard.create('1234', sample_customer.id)
      bank_account = Bank::BankAccount.new(sample_customer.id, 10_000)

      atm = described_class.instance
      atm.register_process(payment_card, bank_account)

      expect(atm.handler).to be_an_instance_of(Bank::Atm::AtmProcessHandler)
    end
  end
end
