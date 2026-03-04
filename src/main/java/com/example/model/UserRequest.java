package main.java.com.example.model;

import lombok.Data;

@Data
public class UserRequest {
    private String username;
    private String email;
    private ProfileInput profile;
}
