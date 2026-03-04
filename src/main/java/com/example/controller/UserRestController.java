package com.example.controller;

import com.example.model.*;
import com.example.service.UserService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserRestController {

    private final UserService userService;

    public UserRestController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public List<User> getAll() {
        return userService.getAllUsers();
    }

    @PostMapping
    public ResponseEntity<User> create(@RequestBody UserRequest request) {
        // Map REST JSON to the same Service method
        User user = userService.createUser(
                request.getUsername(),
                request.getEmail(),
                request.getProfile()
        );
        return ResponseEntity.ok(user);
    }

    @DeleteMapping
    @RequestMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}
