class InputChoiceManager():
    
    def get_valid_input(self, choice_name_list):
        while (True):
            print("")
            print("You have the following options:")

            for i, _choice in enumerate(choice_name_list):
                print("(" + str(i) + ") " + _choice)

            while(True):
                print("")
                _input = input("Please make a selection: ")
                _input = _input.strip()

                _input_lower = _input.lower()
                for i, _choice in enumerate(choice_name_list):
                    if _input_lower == _choice.lower():
                        return i
                    
                _value = self._attempt_to_get_an_int(_input)
                if 0 <= _value and _value < len(choice_name_list):
                    return _value
                
                print("Please try again.")