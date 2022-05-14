db = db.getSiblingDB('kamailio');
db.createCollection('subscribers');
/*
use kamailio;
db.createUser({ user: "root",
          pwd: "root_password",
          roles: [ "dbOwner"]});
*/