import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import LoginPage from "./Pages/LoginPage";
import RegisterPage from "./Pages/RegisterPage";
import ProfilePage from "./Pages/ProfilePage";
import CommunityAllPage from "./Pages/CommunityAllPage";
import CommunityPage from "./Pages/CommunityPage";
import {  BrowserRouter,Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App/>} />
        <Route path="/login" element={<LoginPage/>} />
        <Route path="/register" element={<RegisterPage/>} />
        <Route path="/profile" element={<ProfilePage/>} />
        <Route path="/ar" element={""} />
        <Route path="/communities" element={<CommunityAllPage/>} />
        <Route path="/community" element={<CommunityPage/>} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
reportWebVitals();
