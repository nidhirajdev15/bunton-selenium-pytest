from pageObjects.pom_profile import Profile


class Test_DeleteProfile:
    def test_delete_profile(self, login):
        self.driver, self.wait = login
        self.profile = Profile(self.driver, self.wait)
        self.profile.click_profile_icon()
        self.my_profile = self.profile.click_my_profile()
        self.edit_profile = self.my_profile.profile_click_edit_pencil_icon()
        self.edit_profile.click_more_options()
        self.edit_profile.click_delete_profile()
        self.edit_profile.click_yes_delete_profile()
        self.edit_profile.validate_delete_profile_success()