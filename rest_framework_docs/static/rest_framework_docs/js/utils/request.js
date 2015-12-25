module.exports = {

  shouldAddData: function (method) {
     if (method === 'GET' || method === 'OPTIONS') {
       return true;
     }
     return false;
  },

  shouldAddHeader: function (permissions) {
    if (permissions === 'AllowAny' || permissions === 'None') {
      return true;
    }
    return false;
  }

};
