from TestFramework.Libraries.TestFixture import TestFixture


if __name__ == "__main__":

    testfixture = TestFixture()
    testfixture.setup("chrome")
    testfixture.goto("https://www.youtube.com/watch?v=YDWKZuSVc28")


    testfixture.teardown()

# https://www.youtube.com/watch?v=P8GmToGMeEQ

#D:\Jony\Fiverr\Olik - England\TestAutomation\TestFramework\Libraries\Images\