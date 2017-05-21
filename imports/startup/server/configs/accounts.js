Accounts.validateNewUser((_user) => {
  let loggedInUser = Meteor.user();
  if (Roles.userIsInRole(loggedInUser, 'manage-users', Roles.GLOBAL_GROUP)) {
    return true;
  }

  throw new Meteor.Error(403, 'NotAuthorized to create new users');
});
