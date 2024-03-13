class UserChoiceSelector():
    
    def get_user_choice(self, choice_name_list : list[str]) -> None:
        _index = self._get_choice_index(choice_name_list)
        print("You have selected: (" + str(_index) + ") " + choice_name_list[_index])
        return _index


    def _get_choice_index(self, choice_name_list : list[str]) -> int:
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


    def _attempt_to_get_an_int(self, _input : str):
        try:
            _value = int(_input)
        except:
            return -1
        return _value
