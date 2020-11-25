import {likesApi} from '../../endpoints'

const articleMutations = {
    articleLike: async (_, {id}) => {
        const payload = await likesApi(id);

        if (payload.error) return new Error(JSON.stringify(payload.error))

        const {data} = payload
        return data
    }
}

export default articleMutations
