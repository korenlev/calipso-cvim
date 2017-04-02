import * as R from 'ramda';
import { Roles } from 'meteor/alanning:roles';

let users = [
  {
    username: 'admin',
    name: 'admin',
    email: 'admin@example.com',
    password: 'admin1234',
    roles: ['manage-users', 'manage-link-types']
  }
];

R.forEach((user) => {
  let id;
  let userDb = Meteor.users.findOne({ username: user.username });
  if (R.isNil(userDb)) {
    console.log('creating user', user);
    id = Accounts.createUser({
      username: user.username,
      email: user.email,
      password: user.password,
      profile: { name: user.name }
    });
  } else {
    id = userDb._id;
  }

  if (user.roles.length > 0) {
    console.log('adding roles to user', user, user.roles);
    Roles.addUsersToRoles(id, user.roles, 'default-group');
  }
}, users);