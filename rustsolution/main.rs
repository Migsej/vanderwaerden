use itertools::Itertools;

fn has_arithmetic_progression(group: &mut[usize], k: usize) -> bool {
    group.sort();

    for i in group.iter().combinations(k) {
        let step = i[1] - i[0];
        if (2..k).all(|j| i[j] - i[j - 1] == step) {
            return true;
        }
    }
    return false;


}

fn generaterrest(sum: usize, length: usize) -> Vec<Vec<usize>> {
    if length - 1 == 0 {
        return vec![vec![sum]];
    }

    let mut result = Vec::new();
    for start in 0..sum+1 {
        let rests = generaterrest(sum - start, length -1);
        for i in rests.iter() {
            let mut end = vec![start];
            end.extend(i);
            end.sort();
            if !result.contains(&end) {
                result.push(end);
            }
        }
    }
    return result;
}

fn w(r: usize, k: usize) -> usize {
    let mut n = k;

    loop {
        let numbers = (1..n+1).permutations(n);
        let sizes = generaterrest(n, r);
        let mut found = true;

        for (mut number, size) in numbers.cartesian_product(sizes.iter()) {
            let mut lastindex = 0;
            let mut inddeling = 0;

            for v in size.into_iter() {
                let group = &mut number[lastindex..lastindex+v];
                if has_arithmetic_progression(group, k) {
                    inddeling += 1;
                }
                lastindex = *v;
            }
            if inddeling == 0 {
                found = false;
                break
            }
        }
        if found {
            return n
        }
       
        n += 1;
    }
}

fn main() {
    println!("{}", w(2,3));
}
