import * as actionTypes from "../actions/actions";
const initialState = {
  isLogin: false,
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.LOG_IN: {
      return {
        isLogin: true,
      };
    }
    case actionTypes.LOG_OUT: {
      return {
        isLogin: false,
      };
    }

    default:
      return state;
  }
};

export default reducer;
