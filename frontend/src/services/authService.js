import api from "../api/axios";

export const registerUser = async (userData) => {
    const response = await api.post("/account/register/", userData);

    return response.data;
};

export const loginUser = async (userData) => {
    const response = await api.post("/account/login/", userData);

    return response.data;
};