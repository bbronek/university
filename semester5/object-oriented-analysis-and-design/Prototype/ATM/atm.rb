module Bank
  module Atm
    class Atm
      attr_reader :handler

      @instance = new
      private_class_method :new
      class << self
        attr_reader :instance
      end

      def register_process(card, bank_account)
        @handler = AtmProcessHandler.handle(card, bank_account)
      end
    end
  end
end
