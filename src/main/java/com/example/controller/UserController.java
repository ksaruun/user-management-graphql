package main.java.com.example.controller;

import main.java.com.example.model.Profile;
import main.java.com.example.model.ProfileInput;
import main.java.com.example.model.User;
import main.java.com.example.service.UserService;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.MutationMapping;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.graphql.data.method.annotation.SchemaMapping;
import org.springframework.stereotype.Controller;

import java.util.List;

@Controller
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }
    // --- Queries ---

    @QueryMapping
    public User getUser(@Argument Long id) {
        return userService.getUserById(id);
    }

    @QueryMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    // This method resolves the "profile" field inside the "User" type
    @SchemaMapping(typeName = "User", field = "profile")
    public Profile getProfile(User user) {
        // 'user' is the parent object already fetched by the getUser query
        return user.getProfile();
    }

    // --- Mutations ---

    @MutationMapping
    public User createUser(@Argument String username, @Argument String email) {
        return userService.createUser(username, email, null);
    }

    @MutationMapping
    public boolean deleteUser(@Argument Long id) {
        userService.deleteUser(id);
        return true;
    }

    @MutationMapping
    public User createUserWithProfile(
            @Argument String username,
            @Argument String email,
            @Argument ProfileInput profile
    ) {
        return userService.createUser(username, email, profile);
    }
}