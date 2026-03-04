package main.java.com.example.service;

import jakarta.transaction.Transactional;
import main.java.com.example.model.Profile;
import main.java.com.example.model.ProfileInput;
import main.java.com.example.model.User;
import main.java.com.example.repository.UserRepository;
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