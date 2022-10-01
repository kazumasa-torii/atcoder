require 'json'
require 'net/http'
require 'uri'
require 'set'

class UserFrends
    ORIGINAL_URL = 'https://freundschaft.herokuapp.com/user/'
    def initialize(userId)
        @userId = userId
        @friendIds = UserFriendIds()
    end

    def UserFriendIds()
        res = getUserData(@userId)
        friendIds = res["friends"]
        ids = []
        ids.concat(friendIds)
        for friendId in friendIds do
            frindRes = getUserData(friendId)
            ids.concat(frindRes["friends"])
        end
        return duplicationCheck(ids)
    end

    def getUserData(userId)
        uri = URI("#{ORIGINAL_URL}#{userId}")
        res = Net::HTTP.get(uri)
        return JSON.parse(res)
    end

    def duplicationCheck(ids)
        setIds = Set[*ids]
        return setIds.to_a
    end

    def getFriendNames()
        friendNams = []
        for id in @friendIds do
            friendRes = getUserData(id)
            friendNams.push(friendRes["name"])
        end
        return friendNams
    end
end

userFriend = UserFrends.new(1)
print userFriend.getFriendNames