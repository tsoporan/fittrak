import React from "react";

import MainLayout from "../layouts/Main";

import PageHeaderBar from "../components/Header";
import AppBottomNavigation from "../components/BottomNav";

const Landing = () => {
  return (
    <MainLayout>
      <PageHeaderBar pageTitle="Landing" />
      <div>Body</div>
      <AppBottomNavigation />
    </MainLayout>
  );
};

export default Landing;
