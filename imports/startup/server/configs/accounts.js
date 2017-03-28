Accounts.validateNewUser((user) => {
  let loggedInUser = Meteor.user();
  if (Roles.userIsInRole(loggedInUser, 'manage-users', 'default-group')) {
    return true;
  }

  throw new Meteor.Error(403, 'NotAuthorized to create new users');
});
