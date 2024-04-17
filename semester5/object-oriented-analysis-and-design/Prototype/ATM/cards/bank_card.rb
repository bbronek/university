# frozen_string_literal: true

# top level parent class for handling cards
module Bank
  module Cards
    class BankCard
      attr_reader :pin

      class PinValidator
        class PinCreationError < StandardError; end

        def self.validate(pin)
          errors = []
          errors << PinCreationError.new('Pin must have a length of 4') unless pin.length == 4
          errors << PinCreationError.new('Pin must contain only digits') unless pin.scan(/\D/).empty?

          errors
        end

      end

      def self.create(pin, customer_id)
        new(pin, customer_id) if PinValidator.validate(pin)
      end

      def initialize(pin, customer_id)
        @pin = pin
        @owner_id = customer_id
        @errors = []
      end
    end
  end
end

