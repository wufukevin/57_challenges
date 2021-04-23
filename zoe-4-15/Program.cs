using System;
using System.Collections.Generic;
using BCrypt;

namespace zoe_4_15
{
  class Program
  {
    // static readonly string password = "abc$123";
    static void Main()
    {
      // create user data
      var usr1 = new UserInfo()
      {
        Username = "username1",
        Password = BCrypt.HashPassword("pw1")
      };

      var usr2 = new UserInfo()
      {
        Username = "username2",
        Password = BCrypt.HashPassword("pw2")
      };

      Dictionary<string, UserInfo> users = new();
      users.Add("username1", usr1);
      users.Add("username2", usr2);



      var username = Utils.AskForInputString("who are you ? ");
      var password = Utils.AskForInputString("What is the password ? ");
      var isPass = BCrypt.Verify(password, users[username].Password);

      if (isPass)
        Utils.ConsoleAnswer("Welcome!");
      else
        Utils.ConsoleAnswer("I don't know you.");
    }
  }
}
