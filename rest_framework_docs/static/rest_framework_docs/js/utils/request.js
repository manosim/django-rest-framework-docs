module.exports = {

  shouldIncludeData: function (method) {
    if (method === 'GET' || method === 'OPTIONS') {
      return false;
    }
    return true;
  },

  shouldAddHeader: function (permissions) {
    if (permissions === 'AllowAny') {
      return false;
    }
    return true;
  }

};
