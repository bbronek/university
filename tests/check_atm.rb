require_relative '../semester5/object-oriented-analysis-and-design/prototype/atm/atm'
require_relative '../semester5/object-oriented-analysis-and-design/prototype/atm/cards/payment_card'

card = Bank::Cards::PaymentCard.create('1234', 1)
raise unless Bank::Cards::PaymentCard.create('bad', 1).nil?
raise unless Bank::Cards::PaymentCard.create(nil, 1).nil?
source = Bank::BankAccount.new(1, 100)
target = Bank::BankAccount.new(2, 50)
handler = Bank::Atm::AtmProcessHandler.handle(card, source)
raise unless Bank::Atm::AtmProcessHandler.handle(card, target).nil?
handler.transfer(target, 40)
raise unless source.balance == 60 && target.balance == 90
handler.withdraw(100)
raise unless source.balance == 60 && handler.errors == ['Insufficient funds for withdrawal']
[-1, 0, 0.5].each do |amount|
  begin
    source.withdrawal(amount)
    raise 'Invalid amount accepted'
  rescue ArgumentError
    raise unless source.balance == 60
  end
end
puts 'ATM checks passed'
