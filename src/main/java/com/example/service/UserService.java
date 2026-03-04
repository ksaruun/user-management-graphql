package com.example.service;

import com.example.model.*;
import com.example.repository.UserRepository;
import jakarta.transaction.Transactional;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Transactional
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User createUser(String username, String email, ProfileInput profileInput) {
        User user = new User();
        user.setUsername(username);
        user.setEmail(email);

        if (profileInput != null) {
            Profile profile = new Profile();
            profile.setPhoneNumber(profileInput.getPhoneNumber());
            profile.setAddress(profileInput.getAddress());
            user.setProfile(profile);
            profile.setUser(user);
        }
        return userRepository.save(user);
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public User getUserById(Long id) {
        return userRepository.findById(id).orElseThrow();
    }

    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }
}