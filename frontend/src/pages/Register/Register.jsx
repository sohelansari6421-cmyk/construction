import { useState } from "react";
import { registerUser } from "../../services/authService";
import Input from "../../components/Input/Input";
import Button from "../../components/Button/Button";
import "./Register.css"
function Register() {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        confirm_password: "",
    });

    const [message, setMessage] = useState("");
    const [error, setError] = useState("");

    const handleChange = (event) => {
        const { name, value } = event.target;

        setFormData((previousData) => ({
            ...previousData,
            [name]: value,
        }));
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        setMessage("");
        setError("");

        if (formData.password !== formData.confirm_password) {
            setError("Passwords do not match.");
            return;
        }

        try {
            const data = await registerUser(formData);

            setMessage(data.message);

            setFormData({
                username: "",
                email: "",
                password: "",
                confirm_password: "",
            });
        } catch (error) {
            console.error(error);

            if (error.response?.data) {
                setError(JSON.stringify(error.response.data));
            } else {
                setError("Something went wrong. Please try again.");
            }
        }
    };

    return (
        <div className="register-page">
            <div className="register-container">
                <h1 >Create Account</h1>

                {message && <p className="register-message">{message}</p>}
                {error && <p className="register-error" >{error}</p>}

                <form className="register-form" onSubmit={handleSubmit}>
                    <Input
                        label="Username"
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        placeholder="Enter username"
                    />

                    <Input
                        label="Email"
                        type="email"
                        // name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder="Enter email"
                    />

                    <Input
                        label="Password"
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="Enter password"
                    />

                    <Input
                        label="Confirm Password"
                        type="password"
                        name="confirm_password"
                        value={formData.confirm_password}
                        onChange={handleChange}
                        placeholder="Confirm password"
                    />

                    <Button type="submit">
                        Create Account
                    </Button>
                </form>
            </div>
        </div>
    );
}

export default Register;