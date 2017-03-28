import * as R from 'ramda';

let users = [
  {
    username: 'admin',
    name: 'admin',
    email: 'admin@example.com',
    password: 'admin1234',
    roles: ['manage-users']
  }
];

R.forEach((user) => {
  if (Meteor.users.findOne({ username: user.username })) {
    return;
  }

  console.log('creating user', user);
  id = Accounts.createUser({
    username: user.username,
    email: user.email,
    password: user.password,
    profile: { name: user.name }
  });

  if (user.roles.length > 0) {
    console.log('adding roles to user', user, user.roles);
    Roles.addUsersToRoles(id, user.roles, 'default-group');
  }
}, users);
