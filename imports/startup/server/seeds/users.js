import * as R from 'ramda';
import { Roles } from 'meteor/alanning:roles';

let users = [
  {
    username: 'admin',
    name: 'admin',
    email: 'admin@example.com',
    password: '123456',
    roles: [
      { role: 'manage-users', group: Roles.GLOBAL_GROUP },
      { role: 'manage-link-types', group: Roles.GLOBAL_GROUP },
      { role: 'manage-clique-types', group: Roles.GLOBAL_GROUP },
      { role: 'manage-clique-constraints', group: Roles.GLOBAL_GROUP },
      { role: 'view-env', group: Roles.GLOBAL_GROUP },
      { role: 'edit-env', group: Roles.GLOBAL_GROUP },
    ]
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

    R.forEach((roleItem) => {
      Roles.addUsersToRoles(id, roleItem.role, roleItem.group);
    }, user.roles);
  }
}, users);
